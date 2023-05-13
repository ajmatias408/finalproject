$(document).ready(function() {
  $('#submit').on('click', function(e) {
    e.preventDefault();
    fetchData();
  });
});

function fetchData() {
  const formSerialized = $('#search-form').serialize();
  $('#output').hide();
  $('tbody').empty();

  $.ajax({
    url: './searchquery.cgi',
    dataType: 'json',
    data: formSerialized,
    success: function(response) {
      populateData(response);
    },
    error: function() {
      alert("Error: Unable to find disease.");
    }
  });
}

function populateData(data) {
  let rowIncrement = 1;

  $.each(data.values, function(i, value) {
    var rowId = 'row-' + rowIncrement++;
    $('<tr>', { "id": rowId }).appendTo('tbody');
    $('<td>', { "text": value.SpeciesName + " |" }).appendTo('#' + rowId);
    $('<td>', { "text": value.DOtermName }).appendTo('#' + rowId);
  });

  $('#count').text(data.count);
  $('#output').show();
}
