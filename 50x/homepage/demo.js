let site_index = [
    'index.html',
    '1_All_the',
    '2_Accumulation.html',
    '3_Caliban.html',
    '4_Witchhunt.html',
    '5_Colonization.html',
    '6_Final.html'
    ];



// alert('ok');


function next() {

    current=window.location.pathname.split("/").pop(); // get current page: just last part - page name and extension

    if(site_index.indexOf(current)!==-1) { //check if it is in array
        index= site_index.indexOf(current);
        // alert(index)
    };

    // alert('ok');
    if(index<site_index.length){
        if (index !== 6) {
            next_site=site_index[index+1];
            window.location.href = next_site;
        }
        else {
            alert('This is the last Page, thanks for reading');
        }

        // alert(next_site)

        // console.log(next_site);
    };


};

document.getElementById('next').addEventListener('click', next);
document.getElementById('previous').addEventListener('click', prev);

function prev() {
    current=window.location.pathname.split("/").pop(); // get current page: just last part - page name and extension

    if(site_index.indexOf(current)!==-1) { //check if it is in array
        index= site_index.indexOf(current);
        // alert(index)
    };

    // alert('ok');
    if(index<site_index.length){
        if (index !== 0) {
            next_site=site_index[index-1];
            window.location.href = next_site;
        }
        else {
            alert('There is no previous page, go ahead (:')
        }

        // alert(next_site)

        // console.log(next_site);
    };


};
