var CANVAS = null;
var CTX = null;

window.onload = function () {
    CANVAS = document.getElementById('canvas');
    CTX = CANVAS.getContext('2d');

    CANVAS.addEventListener('click', createPoint);
}

class Point {
    constructor(ctx, pos) {
        /**
         * @param {CanvasRenderingContext2D} ctx
         * @param {Object} pos Contains values for x and y
         */
        this.ctx = ctx;
        this.x = pos.x;
        this.y = pos.y;
    }

    draw() {
        this.ctx.beginPath();
        this.ctx.arc(this.x, this.y, 3, 0, Math.PI*2);
        this.ctx.stroke();
    }
}

class Line {
    constructor(ctx, p1, p2) {
        /**
         * @param ctx
         * @param {Point} p1
         * @param {Point} p2
         */
        this.ctx = ctx;

        this.x1 = p1.x;
        this.y1 = p1.y;
        this.x2 = p2.x;
        this.y2 = p2.y;

        this.connected = false;
    }

    draw() {
        this.ctx.beginPath();
        this.ctx.moveTo(this.x1, this.y1);
        this.ctx.lineTo(this.x2, this.y2);
        this.ctx.stroke();
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
const DRAWHANDLER = new DrawHandler(CTX);

function getMousePos(canvas, evt) {
    // Not called directly via EventListener, takes an Event object to get MousePos
    var rect = canvas.getBoundingClientRect();
    return {
        x: (evt.clientX - rect.left) / (rect.right - rect.left) * canvas.width,
        y: (evt.clientY - rect.top) / (rect.bottom - rect.top) * canvas.height
    };
}

function createPoint(evt) {
    var pos = getMousePos(CANVAS, evt);
    var point = new Point(CTX, pos);
    var line = new Line(CTX, point, pos);
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
    var pos = getMousePos(CANVAS, evt);
    CANVAS.adjustingLine.x2 = pos.x;
    CANVAS.adjustingLine.y2 = pos.y;
    DRAWHANDLER.update();
}

function finishAdjustingLine(evt) {
    // TODO Snap to the nearest point of an existing line; if within a threshold
    CANVAS.adjustingLine.completed = true;
    CANVAS.removeEventListener('mousemove', adjustLine);
    CANVAS.removeEventListener('click', finishAdjustingLine);
    CANVAS.addEventListener('click', createPoint);
    // TODO Add a point to the end of the line, and add it to the DRAWHANDLER
    DRAWHANDLER.update();
    console.log('Finished a Line');
}