import m from "mithril";

var Article = {
    list: [],
    pages: 0,
    page: 1,
    loadList: function() {
        return m.request({
            method: "GET",
            url: "http://kmonitordemo.duckdns.org/api/articles?page="+Article.page,
        })
        .then(function(result) {
            console.log(result)
            Article.list = result.articles
            Article.pages = result.pages
        })
    },
}

export default Article
