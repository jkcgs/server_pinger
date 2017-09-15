(function() {
    'use strict';

    var app = angular.module('app', []);

    app.controller('MainController', MainController);

    MainController.$inject = ['$timeout', 'ServersService'];
    function MainController($timeout, ServersService) {
        var vm = this;
        vm.entries = [];
        activate();

        ////////////////

        function activate() {
            updateData();
        }

        function updateData() {
            ServersService.get().then(function(result) {
                var d = result.data;
                var servers = d.servers.reduce(function(p, c) {
                    p[c.pk] = c.fields;
                    return p;
                }, {});

                vm.entries = result.data.results.map(function(e) {
                    var sv = e.fields.server;
                    e = e.fields;
                    e.server = servers[sv];
                    return e;
                });
            });
            $timeout(updateData, 5000);
        }
    }

    app.service('ServersService', Service);
    Service.$inject = ['$http'];
    function Service($http) {
        this.get = get;

        ////////////////

        function get() {
            return $http.get('/api/servers');
        }
    }
})();