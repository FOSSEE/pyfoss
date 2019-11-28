$(document).ready(function() {
    var pos = 'out';
  var bak = [ '#d7eab0','#27ae60','#34495e'];
    var random = Math.floor(Math.random()*1);
    var $cur = $('.nice-text').eq(random);
    $('.nice-text').hide();
    $cur.show();
    $('.nice-bar').css('background', bak[random]);
    $(".nice-bar").slideDown(function() {
        var i = random;
        setInterval(function() {
            if(pos == 'out') {
                i = (i == 1) ? 0 : ++i; // [0, 1, 2] since 3 events
                $('.nice-text').hide();
                $cur = $('.nice-text').eq(i);
                $('.nice-bar').css('background', bak[i]);
                $cur.show();
            }
        }, 3500);
    });

    $('.nice-bar').mouseenter(function() {
        pos = 'in';
        console.log(pos);
    }).mouseleave(function() {
        pos = 'out';
        console.log(pos);
    });

    $(".nice-close").click(function() {
        $(".nice-bar").slideUp();
    });
});

