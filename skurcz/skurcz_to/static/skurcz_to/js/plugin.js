document.addEventListener('DOMContentLoaded', () => {

  function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');

  document.querySelector('#url-form').onsubmit = () => {

      // Initialize new request
      const request = new XMLHttpRequest();
      const full_url = document.querySelector('#id_full_url').value;
      request.open('POST', 'shorten/');

      // Callback function for when request completes
      request.onload = () => {

          // Extract JSON data from request
          const data = JSON.parse(request.responseText);
          console.log(data)
          // Update the result div
          if (data.success) {
              const short_url = data.short_url
              document.querySelector('#short_url').innerHTML = short_url;
              document.querySelector('#short_url').classList.remove('invisible');
          }
          else {
              document.querySelector('#short_url').innerHTML = 'There was an error.';
          }
      }

      // Add data to send with request
      const data = new FormData();
      data.append('full_url', full_url);
      request.setRequestHeader("X-CSRFToken", csrftoken)
      // Send request
      request.send(data);
      return false;
  };

});
