(function(glob, factory){
	factory(glob, glob.eve);
})(window || this, function(window, eve){
	var Snap = (function(root){
		var glob = {
			win: root.window,
			doc: root.window.document
		};
		glob.win.Snap = Snap;
		return Snap;
	})(window || this);
	
});