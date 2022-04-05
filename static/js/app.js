let dropdown_toggle = document.getElementById('toggle-dropdown')
let dropdown_menu = document.getElementById('dropdown-menu')

let body_element = document.querySelector('body')



let fired_dropdown = false;
dropdown_toggle.addEventListener('click', ()=>{
  fired_dropdown = true;
  dropdown_menu.classList.toggle('active')
})

body_element.addEventListener('click', ()=>{
  if (!fired_dropdown) {
    if (dropdown_menu.classList.contains('active')) {
      dropdown_menu.classList.remove('active')
      }
    }
  fired_dropdown = false
})


// hide message box after
setTimeout(() => {
  const otm_box = document.getElementById('message-box')

  // 👇️ removes element from DOM
  if (otm_box)
    otm_box.style.display = 'none';

}, 5000)


// responsive container height
let navbar = document.querySelector('.navbar')
let container = document.querySelector('.container')


window.addEventListener('resize', ()=> {
  container.style.marginTop = `${navbar.offsetHeight}px`
})


window.addEventListener('load', (event) => {
  container.style.marginTop = `${navbar.offsetHeight}px`
});
