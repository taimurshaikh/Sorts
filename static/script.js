function disableMultiLine(id)
{
  box = document.getElementByID(id);
  box.value = box.value.replace(/\n/g,'');
}
