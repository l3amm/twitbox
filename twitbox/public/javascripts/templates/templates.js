(function() {
  var _ref;

  if ((_ref = window.Templates) == null) {
    window.Templates = {};
  }

  window.Templates['test'] = function(context) {
    return (function() {
      var $o;
      $o = [];
      $o.push("<h1>Hello World</h1>");
      return $o.join("\n");
    }).call(context);
  };

}).call(this);
