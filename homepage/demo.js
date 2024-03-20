function ready() {
    alert('ready ok');
    var site_index = [
        'index.html',
        '1_All_the.html',
        '2_Accumulation.html',
        '3_Caliban.html',
        '4_Witchhunt.html',
        '5_Colonization.html',
        '6_Final.html'
        ];
}

    current=$(location).attr('pathname').substr($(location).attr('pathname').lastIndexOf("/")+1); // get current page: just last part - page name and extension
    if(current.inArray(current, site_index)!==-1) { //check if it is in array
        index=current.inArray(current, site_index);
    }

    function next() {
        alert('ok');
        if(index<site_index.length){
        next=site_index[index+1];
        window.location.href = next;
        }

    }

    document.getElementById('next').addEventListener('click', next);
