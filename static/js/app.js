let dropdown_toggle = document.getElementById('toggle-dropdown')
let dropdown_menu = document.getElementById('dropdown-menu')




dropdown_toggle.addEventListener('click', ()=>{
  console.log('Element Clicked')
  dropdown_menu.classList.toggle('active')
})
