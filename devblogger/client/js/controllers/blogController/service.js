


























// app.service('cakeService', function(){

// 	var cakeArr = [
// 					{
// 						'name':'Jelly',
// 						'frostingflavor': 'vanilla',
// 						'flavor': 'raspberry',
// 						'color': 'red'
// 					},
// 					{
// 						'name':'Voodoo Cake',
// 						'frostingflavor': 'vanilla',
// 						'flavor': 'orange',
// 						'color': 'orange'
// 					},
// 					{
// 						'name':'Bacon Blast',
// 						'frostingflavor': 'Bacon',
// 						'flavor': 'Eggs',
// 						'color': 'Green'
// 					}
// 					];

// 	this.getCakes = function() {
// 		var getC = localStorage.getItem('cakedata');
// 		cakeArr = JSON.parse(getC) || cakeArr;
// 		return cakeArr;
// 	}

// 	function updateLS() {
// 		var str = JSON.stringify(cakeArr);
// 		localStorage.setItem('cakedata', str);
// 	}

// 	this.getCakeAt = function(Idx) {
// 		return this.getCakes()[Idx];
// 	}

// 	this.addCake = function(cake) {
// 		cakeArr.push(cake);
// 		updateLS();
// 	}

// 	this.removeCake = function(cIdx){
// 		cakeArr.splice(cIdx, 1);
// 		updateLS();
// 	}

// 	this.updateCake = function(cake, cIdx) {
// 		cakeArr.splice(cIdx, 1 , cake);
// 		updateLS();
// 	}
// })
















