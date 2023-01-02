


function addIntersectionObserver() {
    

const observer = new IntersectionObserver((a_cards)=>{
    a_cards.forEach((card)=>{

        // console.log(card.isIntersecting);
        if (card.isIntersecting){

            // card.target.firstElementChild.src = card.target.firstElementChild.dataset.src ;
            card.target.classList.remove('a-card_hidden');

        }

        // else
        // card.target.classList.add('a-card_hidden');

    })
});

document.querySelectorAll('#drink_list .a-card').forEach((el)=> observer.observe(el));

}