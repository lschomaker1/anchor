function addMatTableRow() {
  // Get the reference to the table body
  var tableBody = document.getElementById("mat-tbody");

  // Get the reference to the template row
  var templateRow = document.getElementById("mat-row-template");

  // Clone the template row
  var newRow = templateRow.cloneNode(true);

  // Reset the cloned row's ID and style
  newRow.removeAttribute("id");
  newRow.style.display = "";

  // Append the cloned row to the table body
  tableBody.appendChild(newRow);

  // Update the row number in the input field names
  var rowCount = tableBody.childElementCount - 1; // Subtract 1 for the template row
  updateRowNumber(newRow, rowCount);
}

function addRefTableRow() {
  // Get the reference to the table body
  var tbody = document.getElementById("ref-tbody");

  // Clone the row template
  var templateRow = document.getElementById("ref-row-template").cloneNode(true);
  templateRow.style.display = ""; // Make the cloned row visible

  // Modify the cloned row's HTML to assign unique names and IDs
  var rowInputs = templateRow.getElementsByTagName("input");
  var rowSelects = templateRow.getElementsByTagName("select");
  var rowTextarea = templateRow.getElementsByTagName("textarea");
  var rowCounter = tbody.childElementCount;

  for (var i = 0; i < rowInputs.length; i++) {
    var input = rowInputs[i];
    input.name = "refrigerant-" + rowCounter + "-" + input.name;
    input.id = "refrigerant-" + rowCounter + "-" + input.id;
  }

  for (var j = 0; j < rowSelects.length; j++) {
    var select = rowSelects[j];
    select.name = "refrigerant-" + rowCounter + "-" + select.name;
    select.id = "refrigerant-" + rowCounter + "-" + select.id;
  }

  for (var k = 0; k < rowTextarea.length; k++) {
    var textarea = rowTextarea[k];
    textarea.name = "refrigerant-" + rowCounter + "-" + textarea.name;
    textarea.id = "refrigerant-" + rowCounter + "-" + textarea.id;
  }

  // Append the modified cloned row to the table body
  tbody.appendChild(templateRow);

  // Update the row number in the input field names
  updateRowNumber(templateRow, rowCounter);
}

// Update the row number in the input field names
function updateRowNumber(row, rowNumber) {
  var inputs = row.getElementsByTagName("input");
  for (var i = 0; i < inputs.length; i++) {
    var name = inputs[i].getAttribute("name");
    var updatedName = name.replace(/-\d+-/, "-" + rowNumber + "-");
    inputs[i].setAttribute("name", updatedName);
  }
}

function renderSignature(signatureData) {
  var canvas = document.getElementById('signatureCanvas');
  var ctx = canvas.getContext('2d');

  // Clear the canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Parse the signature data
  var signature = JSON.parse(signatureData);

  // Render the signature on the canvas
  ctx.beginPath();
  ctx.moveTo(signature.x[0], signature.y[0]);
  for (var i = 1; i < signature.x.length; i++) {
    ctx.lineTo(signature.x[i], signature.y[i]);
  }
  ctx.stroke();
}

function deleteSelectedMatRows() {
  var matTableBody = document.getElementById('mat-tbody');
  var rows = matTableBody.getElementsByTagName('tr');

  // Iterate over the rows in reverse order
  for (var i = rows.length - 1; i >= 0; i--) {
    var checkbox = rows[i].querySelector('input[name^="material-"][name$="-delete"]');

    // Check if the checkbox is checked
    if (checkbox && checkbox.checked) {
      // Remove the row
      rows[i].remove();
    }
  }
}

function deleteSelectedRefRows() {
  var refTableBody = document.getElementById('ref-tbody');
  var rows = refTableBody.getElementsByTagName('tr');

  // Iterate through the rows in reverse order
  for (var i = rows.length - 1; i >= 0; i--) {
    var deleteCheckbox = rows[i].querySelector('input[name^="refrigerant-"][name$="-delete"]');

    // Delete the row if the delete checkbox is checked
    if (deleteCheckbox && deleteCheckbox.checked) {
      refTableBody.removeChild(rows[i]);
    }
  }
}

document.addEventListener('DOMContentLoaded', function () {
  var deleteMatBtn = document.getElementById('delete-mat-rows-btn');
  if (deleteMatBtn) {
    deleteMatBtn.addEventListener('click', deleteSelectedMatRows);
  }

  var deleteRefBtn = document.getElementById('delete-ref-rows-btn');
  if (deleteRefBtn) {
    deleteRefBtn.addEventListener('click', deleteSelectedRefRows);
  }

});

function submitForms() {
  var materialForm = document.getElementById('material-form');
  var refrigerantForm = document.getElementById('refrigerant-form');
  
  // Remove the deletion checkboxes before submitting the forms
  removeDeletionCheckboxes(materialForm);
  removeDeletionCheckboxes(refrigerantForm);
  
  // Submit the material form
  materialForm.submit();
  
  // Submit the refrigerant form
  refrigerantForm.submit();
}

// Remove the deletion checkboxes before submitting the form
function removeDeletionCheckboxes(form) {
  var checkboxes = form.querySelectorAll('input[name$="-delete"]');
  checkboxes.forEach(function (checkbox) {
    checkbox.parentNode.removeChild(checkbox);
  });
}