/** 
 * ===================================
 * 
 * Global Variables
 * 
 * ===================================
 */

var STARTINGID = 0;
var CANVAS = null;
var CTX = null;
var DRAWHANDLER = null;
var SNAPTOGRID = true;
var SNAPTOLINES = true;
var UNDOHISTORY = [];

/**
 * ===================================
 * 
 * Class Definitions
 * 
 * ===================================
 */

class Point {
    constructor(pos, size=3, color='#000000') {
        /**
         * @param {Object} pos Contains values for x and y
         */
        this.ctx = CTX;
        this.x = pos.x;
        this.y = pos.y;
        this.size = size;
        this.color = color;
        this.id = STARTINGID;
        STARTINGID++;
    }

    draw() {
        this.ctx.lineWidth = this.size;
        this.ctx.strokeStyle = this.color;
        this.ctx.fillStyle = this.color;
        this.ctx.beginPath();
        this.ctx.arc(this.x, this.y, this.size * 2, 0, Math.PI*2);
        this.ctx.fill();
        this.ctx.stroke();
    }
}

class Line {
    constructor(p1, p2, size=3, color='#000000', showPoints=true) {
        /**
         * A line segment, with a point on either end
         * @param {Point} p1
         * @param {Point} p2
         */
        this.ctx = CTX;
        this.p1 = p1;
        this.p2 = p2;
        this.showPoints = showPoints;
        this.size = size;
        this.color = color;
        this.connected = false;
        this.length = null;
        this.id = STARTINGID;
        STARTINGID++;
    }

    draw() {
        if (this.showPoints) {
            this.p1.draw();
            this.p2.draw();
        }
        this.ctx.lineWidth = this.size;
        this.ctx.strokeStyle = this.color;
        this.ctx.beginPath();
        this.ctx.moveTo(this.p1.x, this.p1.y);
        this.ctx.lineTo(this.p2.x, this.p2.y);
        this.ctx.stroke();
    }
}

class Grid {
    constructor(canvas, size, showLines=true, showPoints=true) {
        this.ctx = CTX;
        this.canvas = canvas;
        this.size = size;
        this.points = [];
        // Initialize Points for a 2D Grid
        for (var i = 0; i < this.canvas.height; i += size) {
            for (var j = 0; j < this.canvas.width; j += size) {
                this.points.push(new Point(
                    {x: j, y: i}, // Basic x & y object
                    1, '#ffffff'  // Optional Params
                ));
            }
        }
        this.lines = [];
        // Initialize Horizontal Lines
        for (var i = 0; i < this.canvas.height; i += size) {
            this.lines.push(new Line(
                new Point({x: 0, y: i}),                 // p1
                new Point({x: this.canvas.width, y: i}), // p2
                1, '#ffffff', false                      // Optional Params
            ));
        }
        // Vertical Lines
        for (var i = 0; i < this.canvas.width; i += size) {
            this.lines.push(new Line(
                new Point({x: i, y: 0}),                  // p1
                new Point({x: i, y: this.canvas.height}), // p2
                1, '#ffffff', false                       // Optional Params
            ));
        }
        this.showPoints = showPoints;
        this.showLines = showLines;
    }

    draw() {
        if (this.showPoints) {
            this.points.forEach(point => point.draw());
        }
        if (this.showLines) {
            this.lines.forEach(line => line.draw());
        }
    }
}

class DrawHandler {
    constructor() {
        this.ctx = CTX;
        // elements list is changed on undo and redo
        this.elements = [];
        // persistent elements should not be referenced during an undo and redo
        this.persistentElements = [];
    }

    pushPersistent(element) {
        this.persistentElements.push(element);
        this.update();
    }

    push(element) {
        this.elements.push(element);
        this.update();
    }

    pop() {
        var removedElement = this.elements.pop();
        this.update();
        return removedElement
    }

    update() {
        CTX.clearRect(0, 0, this.ctx.canvas.width, this.ctx.canvas.height);
        this.persistentElements.forEach(element => element.draw());
        this.elements.forEach(element => element.draw());
    }
}

/**
 * ===================================
 * 
 * Setup
 * 
 * ===================================
 */

window.onload = function () {
    CANVAS = document.getElementById('canvas');
    CTX = CANVAS.getContext('2d');

    // Initial EventListeners
    CANVAS.addEventListener('click', startLine);
    document.onkeydown = keyPress;

    // The DRAWHANDLER refreshes the screen when a new element is added
    // DRAWHANDLER also stores a list of existing elements
    DRAWHANDLER = new DrawHandler();
    var grid = new Grid(CANVAS, 50);
    DRAWHANDLER.pushPersistent(grid);
}

/**
 * ===================================
 * 
 * Function Definitions
 * 
 * ===================================
 */

function keyPress(evt) {
    var evtobj = window.event ? event : evt;
    if (evtobj.keyCode == 90 && evtobj.ctrlKey) { // Ctrl+z
        undo();
    }
    if (evtobj.keyCode == 89 && evtobj.ctrlKey) { // Ctrl+y
        redo();
    }
    if (evtobj.key == 'Escape') { // Escape
        cancelLine();
    }
}

function undo() {
    var removedElement = DRAWHANDLER.pop();
    if (!removedElement) return;
    UNDOHISTORY.push(removedElement);
}

function redo() {
    var newElement = UNDOHISTORY.pop();
    if (!newElement) return;
    DRAWHANDLER.push(newElement);
}

function getMousePos(canvas, evt) {
    // Not called directly via EventListener, takes an Event object to get MousePos
    var rect = canvas.getBoundingClientRect();
    return {
        x: (evt.clientX - rect.left) * (canvas.width / rect.width),
        y: (evt.clientY - rect.top) * (canvas.height / rect.height)
    };
}

function startLine(evt) {
    // TODO Snap to the nearest point of an existing line; if within a threshold
    // TODO Snap to the nearest point on a grid, if grid snapping is enabled
    var pos = getMousePos(CANVAS, evt);
    var line = new Line(new Point(pos), new Point(pos), 8);
    CANVAS.adjustingLine = line;
    DRAWHANDLER.push(line);
    UNDOHISTORY = [];

    CANVAS.removeEventListener('click', startLine);
    CANVAS.addEventListener('mousemove', adjustLine);
    CANVAS.addEventListener('click', finishAdjustingLine);
}

function cancelLine(evt) {
    if (!CANVAS.adjustingLine.completed) {
        DRAWHANDLER.pop();
        CANVAS.removeEventListener('mousemove', adjustLine);
        CANVAS.removeEventListener('click', finishAdjustingLine);
        CANVAS.addEventListener('click', startLine);
    }
}

function adjustLine(evt) {
    var pos = getMousePos(CANVAS, evt);
    CANVAS.adjustingLine.p2.x = pos.x;
    CANVAS.adjustingLine.p2.y = pos.y;
    DRAWHANDLER.update();
}

function finishAdjustingLine(evt) {
    var pos = getMousePos(CANVAS, evt);
    // TODO Snap to the nearest point of an existing line; if within a threshold
    // TODO Snap to the nearest point on a grid, if grid snapping is enabled
    CANVAS.adjustingLine.completed = true;
    // TODO Add a textbox to the center of the line for length
    // Attach this textbox to edit the CANVAS.adjustingLine.length
    DRAWHANDLER.update();

    CANVAS.removeEventListener('mousemove', adjustLine);
    CANVAS.removeEventListener('click', finishAdjustingLine);
    CANVAS.addEventListener('click', startLine);
}