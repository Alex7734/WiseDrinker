var app = new Vue({
    delimiters: ["[[", "]]"],
    el: "#app",
    data: {
        drunk_level: {{request.session.drunk_level}}
    },
    methods: {
        vote: function() {
            alert('Hello there!')
        }
    }
});