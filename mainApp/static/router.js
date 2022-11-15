


const populatePage = {

    '/': ()=> { return undefined },
    '/browse': ()=> { return undefined },
  
    '/drink': ()=> update_drinkPage(),
  
  }

  
  function navigate_to( newUrl ){
  
    history.pushState( {}, "", newUrl );
  
    // let newPage = window.location.pathname;
    loadPage();
  
  }
  
  
function loadPage(){
  
    let newPage = window.location.pathname;
    // console.log(window.location.pathname);
    let newPage_div = document.querySelector( `[data-page = "${newPage}"` );
    console.log(newPage_div);
  
    document.querySelectorAll('.page').forEach((page)=> page.style['opacity'] = '0')
    
    // populatePage[newPage]() || populatePage['default']();
    populatePage[newPage]();
  
    setTimeout(()=>{
  
      document.querySelectorAll('.page').forEach((page)=> page.style['display'] = 'none')
      newPage_div.style['display'] = 'flex';
      
      setTimeout(()=> newPage_div.style['opacity'] = '1', 11);
  
  
    },400);
  }

  
  
  window.addEventListener("popstate", event => {
  
                  // Grab the history state id
                  // let prev_state = event.state;
  
                  // console.log(new URLSearchParams(window.location.search).keys);
                  // Visually select the clicked button/tab/box
                  // select_tab(stateId);
                  // Load content for this tab/page
                  // load_content(stateId);
  
                  loadPage()
              });
  
  
  loadPage();