let label = [0];
let temperature_data = [0];
let pulse_data = [0];
let spO2_data = [0];
let pi_data = [0];
var a = 0;

var ctx1 = document.querySelector('#temp');
var ctx2 = document.querySelector('#pulse');
var ctx3 = document.querySelector('#spo2');
var ctx4 = document.querySelector('#pi');

var tempChart = new Chart(ctx1, {
  type: 'line',
  data: {
    labels:label,
    datasets: [{
      data: temperature_data,
      backgroundColor: [
        'rgba(255, 223, 37, 0.3)'
      ],
      borderColor: [
        'rgba(180, 154, 0, 1)'
      ],
      borderWidth: 3
    }]
  },
  options: {
    legend: {
      display: false
    }
  }
});

var pulseChart = new Chart(ctx2, {
  type: 'line',
  data: {
    labels:label,
    datasets: [{
      data: pulse_data,
      backgroundColor: [
        'rgba(65, 255, 68, 0.3)'
      ],
      borderColor: [
        'rgba(0, 180, 3, 1)'
      ],
      borderWidth: 3
    }]
  },
  options: {
    legend: {
      display: false
    }
  }
});

var spo2Chart = new Chart(ctx3, {
  type: 'line',
  data: {
    labels:label,
    datasets: [{
      data: spO2_data,
      backgroundColor: [
        'rgba(49, 244, 255, 0.3)'
      ],
      borderColor: [
        'rgba(0, 170, 180, 100)'
      ],
      borderWidth: 3
    }]
  },
  options: {
    legend: {
      display: false
    }
  }
});

var piChart = new Chart(ctx4, {
  type: 'line',
  data: {
    labels:label,
    datasets: [{
      data: pi_data,
      backgroundColor: [
        'rgba(199, 49, 255, 0.3)'
      ],
      borderColor: [
        'rgba(113, 0, 156, 1)'
      ],
      borderWidth: 3
    }]
  },
  options: {
    legend: {
      display: false
    }
  }
});


function refreshData() {
  var XHR = ("onload" in new XMLHttpRequest()) ? XMLHttpRequest : XDomainRequest;
  var xhr = new XHR();

	xhr.open('GET', 'http://192.168.2.102:5000/data' , true);

  xhr.onreadystatechange=function() {
  if (xhr.readyState==4 && xhr.status ==200) {
    var data=JSON.parse(xhr.responseText);


    console.log(data);
    a = a + 1;
    if (temperature_data.length >= 10){
      label.shift();
      temperature_data.shift();
      pulse_data.shift();
      spO2_data.shift();
      pi_data.shift();
      label.push(a);
      temperature_data.push(data.temperature);
      pulse_data.push(data.pulse);
      spO2_data.push(data.spO2);
      pi_data.push(data.pi);
    }
    else{
      label.push(a);
      temperature_data.push(data.temperature);
      pulse_data.push(data.pulse);
      spO2_data.push(data.spO2);
      pi_data.push(data.pi);
    }
    tempChart.update();
    pulseChart.update();
    spo2Chart.update();
    piChart.update();


    document.querySelector('#h5temp').innerHTML = 'Температура: '+ data.temperature+'°'
    document.querySelector('#h5pulse').innerHTML = 'Пульс: '+ data.pulse+' уд/мин'
    document.querySelector('#h5spO2').innerHTML = 'SpO2: '+ data.spO2+'%'
    document.querySelector('#h5pi').innerHTML = 'PI: '+ data.pi+'%'
    }
  }
  xhr.send();
}



setInterval(refreshData, 1500);
