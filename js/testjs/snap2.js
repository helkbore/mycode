function Snap(w, h) {
    console.log('snap');
	w = document.querySelector(String(w));
	return wrap(w);

}

function wrap(dom) {
	console.log('wrap');
    return new Paper(dom);
}

function Paper(w, h) {
	console.log('paper');
	console.log(Paper.prototype);
    var res,
        desc,
        defs,
        proto = Paper.prototype;

	var doc = w.ownerDocument;
	res = new Element(w);


	res.defs = defs;
	for (var key in proto) if (proto[has](key)) {
		res[key] = proto[key];
	}
	res.paper = res.root = res;

    return res;
}

function Element(el) {
    var svg;
    try {
        svg = el.ownerSVGElement;
    } catch(e) {}
    /*\
* Element.node
[ property (object) ]
**
* Gives you a reference to the DOM object, so you can assign event handlers or just mess around.
> Usage
| // draw a circle at coordinate 10,10 with radius of 10
| var c = paper.circle(10, 10, 10);
| c.node.onclick = function () {
|     c.attr("fill", "red");
| };
\*/
    this.node = el;
    if (svg) {
        this.paper = new Paper(svg);
    }
    /*\
* Element.type
[ property (string) ]
**
* SVG tag name of the given element.
\*/
    this.type = el.tagName || el.nodeName;
    var id = this.id = "svg123";
    this.anims = {};
    this._ = {
        transform: []
    };
    el.snap = id;


}