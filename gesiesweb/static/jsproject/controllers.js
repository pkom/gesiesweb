(function () {
    angular.module('gesiesweb.controllers', [])
    .controller('ParteCtrl', ['$scope', function ($scope) {
               $scope.datos = {
                   partesTotales : 120
               };
    }])
})();