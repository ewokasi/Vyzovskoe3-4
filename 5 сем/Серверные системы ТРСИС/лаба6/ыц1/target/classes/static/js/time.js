var app = angular.module('time', []);

app.controller("TtApiController", function( $scope, $http){

    $scope.getTt = function (){
        $http.get('/api/v3/tt').success(function (data, status, headers, config){
            $scope.ttList = data;
            console.log($scope.ttList)
        }).error(function (data, status, headers, config){
            if (data.message === 'Time is out'){
                $scope.finishByTimeout();
                console.log('Errorrrr')
            }
        });
    };
});