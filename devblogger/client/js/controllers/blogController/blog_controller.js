app.controller('DevBlogController', ['$scope', '$resource','$route',function($scope, $resource){
    var DevPost = $resource('/api/posts');
    DevPost.query(function(results){
        $scope.devblogs = results;
    })
    $scope.devblogs = [];
    $scope.createBlogPost = function() {
        var postDev = new DevPost();
        postDev.name = $scope.postName;
        postDev.$save(function(result){
            $scope.devblogs.push(result);
            $scope.postName = '';
        });
    }
}]);


// app.controller('EditController', function($scope, cakeService, $routeParams){
//     $scope.cake = angular.copy(cakeService.getCakeAt($routeParams.cakeIdx));
//     $scope.onSubmit = function() {
//         cakeService.updateCake($scope.cake, $routeParams.cakeIdx);
//         $scope.cake = {};
//         document.location.hash = "#/list";
//     }
// });

// app.exports.create = function(req, res) {
//     console.log(req.body);
// }























// app.config(function($routeProvider){
//     $routeProvider
//         .when('/list', {
//             'controller': 'ListController',
//             'templateUrl': '/views/list.html'
//         })
//         .when('/new', {
//             'controller': 'NewCakeController',
//             'templateUrl': '/views/form.html'
//         })
//         .when('/detail/:cakeIdx', {
//             'controller': 'DetailController',
//             'templateUrl': '/views/detail.html'
//         })
//         .when('/edit/:cakeIdx', {
//             'controller': 'EditController',
//             'templateUrl': '/views/form.html'
//         })
//         .otherwise({
//             'redirectTo': '/list'
//         })
// });

// app.controller('ListController', function($scope, cakeService){
//     $scope.cakes = cakeService.getCakes();
// });

// app.controller('NewCakeController', function($scope, cakeService){
//     $scope.cake = {};
//     $scope.onSubmit = function() {
//         cakeService.addCake($scope.cake);
//         $scope.cake = {};
//         document.location.hash = "#/list";
//     }
// });

// app.controller('DetailController', function($scope, cakeService, $routeParams){
//     $scope.cake = cakeService.getCakeAt($routeParams.cakeIdx);
//     $scope.cakeIdx = $routeParams.cakeIdx;
//     $scope.remove = function() {
//         cakeService.removeCake($routeParams.cakeIdx);
//         document.location.hash = "#/list";
//     }
// });

// app.controller('EditController', function($scope, cakeService, $routeParams){
//     $scope.cake = angular.copy(cakeService.getCakeAt($routeParams.cakeIdx));
//     $scope.onSubmit = function() {
//         cakeService.updateCake($scope.cake, $routeParams.cakeIdx);
//         $scope.cake = {};
//         document.location.hash = "#/list";
//     }
// });