function copyToClipboard() {
    //select the element with the id "copyMe", must be a text box
    var textToCopy = document.getElementById("shorturl");
    //select the text in the text box
    textToCopy.select();
    //copy the text to the clipboard
    document.execCommand("copy");
}