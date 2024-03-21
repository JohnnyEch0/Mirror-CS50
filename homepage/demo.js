let site_index = [
    'index.html',
    '1_All_the.html',
    '2_Accumulation.html',
    '3_Caliban.html',
    '4_Witchhunt.html',
    '5_Colonization.html',
    '6_Final.html'
    ];



// alert('ok');


function next() {

    current=$(location).attr('pathname').substr($(location).attr('pathname').lastIndexOf("/")+1); // get current page: just last part - page name and extension
    if(site_index.indexOf(current)!==-1) { //check if it is in array
        index= site_index.indexOf(current);
    };

    alert('ok');
    if(index<site_index.length){
        next_site=site_index[index+1];
        window.location.href = next_site;
    };


}

    document.getElementById('next').addEventListener('click', next);
