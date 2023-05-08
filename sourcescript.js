async function fetchData(search_input, query) {
  const response = await fetch(`http://bfx3.aap.jhu.edu/amatias1/final/sourcecode.py?search_input=${search_input}&query=${query}`);
  const data = await response.json();
  return data;
}

document.getElementById('search-form').addEventListener('submit', async (event) => {
  event.preventDefault();
  const search_input = document.getElementById('search-input').value;
  const data = await fetchData(search_input, 'gene_term');

  const resultsDiv = document.getElementById('results');
  resultsDiv.innerHTML = '';

  data.values.forEach(value => {
    const resultElement = document.createElement('div');
    resultElement.textContent = `SpeciesName: ${value.SpeciesName}, DBObjectSymbol: ${value.DBObjectSymbol}, DOtermName: ${value.DOtermName}`;
    resultsDiv.appendChild(resultElement);
  });
});
