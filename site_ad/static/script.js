function showProducts(category) {
  // Переход на страницу с категорией

    window.location.href = `/${category}/`;

}
// Экранирование ввода телефона
function restrictPhoneInput(input) {

  input.value = input.value.replace(/[^0-9+]/g, '');


  if (input.value.length > 1) {
    if (input.value[0] === '+' || /^\d$/.test(input.value[0])) {
      input.value = '+' + input.value.slice(0).replace(/\+/g, '');
    } else {
      input.value = input.value.slice(0);
    }
  }
   if (input.value.length > 14) {
    input.value = input.value.slice(0, 14);
  }
}
// Автоматическое расширение поля описания при большом количестве текста
 function adjustTextAreaHeight(textarea) {
    textarea.style.height = "auto";
    textarea.style.height = textarea.scrollHeight + "px";
  }

  document.addEventListener("DOMContentLoaded", function() {
    var descriptionTextArea = document.getElementById("id_description");
    descriptionTextArea.addEventListener("input", function() {
      adjustTextAreaHeight(this);
    });
  });