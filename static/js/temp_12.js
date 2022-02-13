var change = {{bourse_status.change}};

if (change > 0) {
    document.getElementsByName("number").style.color="#ff4698";
}

else if (change < 0) {
    document.getElementsByName("number").style.color="#6bd98b";
}