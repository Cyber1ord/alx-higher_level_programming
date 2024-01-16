$(function() {
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    method: "GET",
    success: function(response) {
      var movies = response.results;
      var list = $("UL#list_movies");
      $.each(movies, function(index, movie) {
        var title = $("<li>").text(movie.title);
        list.append(title);
      });
    }
  });
});
