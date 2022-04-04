let dropdown_toggle = document.getElementById('toggle-dropdown')
let dropdown_menu = document.getElementById('dropdown-menu')




dropdown_toggle.addEventListener('click', ()=>{
  console.log('Element Clicked')
  dropdown_menu.classList.toggle('active')
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
