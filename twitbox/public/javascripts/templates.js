(function() {

  if (window.Templates == null) {
    window.Templates = {};
  }

  window.Templates['test'] = function(context) {
    return (function() {
      var $o;
      $o = [];
      $o.push("<h1>Hello World</h1>");
      return $o.join("\n").replace(/\s(\w+)='true'/mg, ' $1').replace(/\s(\w+)='false'/mg, '');
    }).call(context);
  };

}).call(this);
