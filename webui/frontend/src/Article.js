import m from "mithril";

var Article = {
    list: [],
    loadList: function() {
        return m.request({
            method: "GET",
            url: "http://kmonitordemo.duckdns.org/api/articles",
        })
        .then(function(result) {
            Article.list = result
        })
    },
}

export default Article
