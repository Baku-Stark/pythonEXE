const search_form = document.querySelector(".search_form");

function set_result(data){
  const set_ip = document.querySelector(".set_ip");
  const org = document.querySelector(".result_org");
  const continent = document.querySelector(".result_continent");
  const country = document.querySelector(".result_country");
  const city = document.querySelector(".result_city");
  const time_zone = document.querySelector(".result_tz");

  set_ip.innerHTML = `${data.query} - ${data.isp}`;
  org.innerHTML = `${data.org}`
  continent.innerHTML = `${data.continent}-${data.continentCode}`
  country.innerHTML = `${data.country}-${data.countryCode}`;
  city.innerHTML = `${data.city}, ${data.regionName}-${data.region}`;
  time_zone.innerHTML = `${data.timezone}`;
}

search_form.addEventListener("submit", async (e) => {
  e.preventDefault();

  var user_ip = document.querySelector("#search_ip").value;
  
  await fetch(`/user_ip_address_=${user_ip}`, {
    method: "GET"
  })
  .then((response) => response.json())
  .then((data) => {
      set_result(data);
    })
})