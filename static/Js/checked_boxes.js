<script type="text/javascript">


reload();
//alert('sddssd')

//add click functionality to radio buttons
Array.from(document.querySelectorAll('input[type="radio"]')).forEach(function(item, index) {
  item.addEventListener('click', save);
});

//Save Values
function save() {
  //Radiobuttons  
  var g1 = document.querySelector('input[name=tabs]:checked');
  g1 = (g1) ? g1.value : '';
  localStorage.setItem("g1", g1);
}
//Restoring saved Values
function reload() {
  // Radiobuttons    
  // get a list of DOM elements
  var G1 = Array.from(document.getElementsByName('tabs'));
  var val1 = localStorage.getItem('g1');
  for (var i = 0; i < G1.length; i++) {
    if (G1[i].value == val1) {
      G1[i].checked = true;
    }
  }
}



</script>