(function () {

    var gesieswebApp = angular.module('gesieswebApp',[
    'gesiesweb.controllers',
    'gesiesweb.services'
    ]);

    gesieswebApp.config(function($interpolateProvider){
        $interpolateProvider.startSymbol('[[')
            .endSymbol(']]');
    });

})();