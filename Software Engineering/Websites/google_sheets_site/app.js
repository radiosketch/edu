/**
 * ==============================
 * 
 * Class Definitions
 * 
 * ==============================
 */

class Point {
    constructor(ctx, pos, size=3, color='#000000') {
        /**
         * @param {CanvasRenderingContext2D} ctx
         * @param {Object} pos Contains values for x and y
         */
        this.ctx = ctx;

        this.x = pos.x;
        this.y = pos.y;

        this.size = size;
        this.color = color;
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
    constructor(ctx, p1, p2, size=3, color='#000000') {
        /**
         * @param ctx
         * @param {Point} p1
         * @param {Point} p2
         */
        this.ctx = ctx;

        this.p1 = p1;
        this.p2 = p2;

        this.size = size;
        this.color = color;

        this.connected = false;

        this.length = null;
    }

    draw() {
        this.ctx.lineWidth = this.size;
        this.ctx.strokeStyle = this.color;
        this.ctx.beginPath();
        this.ctx.moveTo(this.p1.x, this.p1.y);
        this.ctx.lineTo(this.p2.x, this.p2.y);
        this.ctx.stroke();
    }
}

class Grid {
    constructor(ctx, canvas, size) {
        this.ctx = ctx;
        this.canvas = canvas;
        this.size = size;

        this.points = [];
        for (var i = 0; i < this.canvas.height; i += size) {
            for (var j = 0; j < this.canvas.width; j += size) {
                this.points.push(new Point(
                    this.ctx,
                    {x: j, y: i},
                    1,
                    '#ffffff'
                ));
            }
        }

        this.lines = [];
        // Horizontal Lines
        for (var i = 0; i < this.canvas.height; i += size) {
            this.lines.push(new Line(
                this.ctx,
                {x: 0, y: i},                 // p1
                {x: this.canvas.width, y: i}, // p2
                1,
                '#ffffff'
            ));
        }
        // Vertical Lines
        for (var i = 0; i < this.canvas.width; i += size) {
            this.lines.push(new Line(
                this.ctx,
                {x: i, y: 0},                  // p1
                {x: i, y: this.canvas.height}, // p2
                1,
                '#ffffff'
            ));
        }

        this.showPoints = true;
        this.showLines = true;
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
    constructor(ctx) {
        this.ctx = ctx;
        this.elements = [];
        this.startingId = 0;
    }

    add(element) {
        this.elements.push({shape: element, id: this.startingId});
        this.startingId += 1;
    }

    remove(elementId) {
        this.elements = this.elements.filter(element => element.id != elementId);
    }

    update() {
        CTX.clearRect(0, 0, CTX.canvas.width, CTX.canvas.height);
        this.elements.forEach(element => element.shape.draw());
    }
}

/**
 * ==============================
 * 
 * Function Definitions
 * 
 * ==============================
 */

// Global variables
var CANVAS = null;
var CTX = null;
var DRAWHANDLER = null;

// Setup
window.onload = function () {
    CANVAS = document.getElementById('canvas');
    CTX = CANVAS.getContext('2d');

    CANVAS.addEventListener('click', createPoint);

    DRAWHANDLER = new DrawHandler(CTX);
    var grid = new Grid(CTX, CANVAS, 50);
    grid.showPoints = false;
    DRAWHANDLER.add(grid);
    DRAWHANDLER.update();
}

function getMousePos(canvas, evt) {
    // Not called directly via EventListener, takes an Event object to get MousePos
    var rect = canvas.getBoundingClientRect();
    return {
        x: (evt.clientX - rect.left) * (canvas.width / rect.width),
        y: (evt.clientY - rect.top) * (canvas.height / rect.height)
    };
}

function createPoint(evt) {
    // TODO Snap to the nearest point of an existing line; if within a threshold
    // TODO Snap to the nearest point on a grid, if grid snapping is enabled
    var pos = getMousePos(canvas, evt);
    var point = new Point(CTX, pos);
    var line = new Line(CTX, point, pos, 8);
    if (!line.completed) {
        CANVAS.removeEventListener('click', createPoint);
        CANVAS.addEventListener('mousemove', adjustLine);
        CANVAS.addEventListener('click', finishAdjustingLine);
        CANVAS.adjustingLine = line;
    }
    point.draw();

    DRAWHANDLER.add(point);
    DRAWHANDLER.add(line);
    console.log('Started a Line');
}

function adjustLine(evt) {
    var pos = getMousePos(canvas, evt);
    CANVAS.adjustingLine.p2 = pos;
    DRAWHANDLER.update();
}

function finishAdjustingLine(evt) {
    // TODO Snap to the nearest point of an existing line; if within a threshold
    // TODO Snap to the nearest point on a grid, if grid snapping is enabled
    var pos = getMousePos(canvas, evt);

    CANVAS.adjustingLine.completed = true;
    CANVAS.removeEventListener('mousemove', adjustLine);
    CANVAS.removeEventListener('click', finishAdjustingLine);
    CANVAS.addEventListener('click', createPoint);

    // Add a point at the end of the line
    var point = new Point(CTX, pos);
    DRAWHANDLER.add(point);

    // TODO Add a textbox to the center of the line for length
    // Attach this textbox to edit the CANVAS.adjustingLine.length

    DRAWHANDLER.update();
    console.log('Finished a Line');
}