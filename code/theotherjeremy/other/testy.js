(document).readyState(function () {
    (document).scroll(function () {
        while ((window.pageYOffset + window.innerHeight) >= $this.height() - (window.innerHeight / 2)) {
            ('ul').append('<li>Testing.</li>');
        }


    }).scroll();
    fartscroll(200);
});



