function executeQuery() {
  $('#output').hide();
  $('tbody').empty();
  var inputToString = $('#search-form').serialize();
  console.log(inputToString);

  $.ajax({
    url: 'searchquery.cgi',
    dataType: 'json',
    data: inputToString,
    success: function (data, jqXHR) {
      executeJSON(data);
    },
    error: function (jqXHR, errorThrown) {
      alert("Unable to find disease.");
    }
  });
}

function executeJSON(data) {
  $('#count').text(data.count);
  var succeeding_row = 1;
  $.each(data.values, function (i, item) {
    var current_row = succeeding_row++;
    $('<tr/>', { id: current_row }).appendTo('tbody');
    $('<td/>', { text: item.SpeciesName }).appendTo('#' + current_row);
    $('<td/>', { text: item.DOtermName }).appendTo('#' + current_row);
  });
  $('#output').show();
}

$(document).ready(function () {
  $('#submit').click(function () {
    executeQuery();
    return false;
  });
});
