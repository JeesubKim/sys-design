import './Header.scss'

interface HeaderType{

    displayName:string
    link:string
}

interface Props {
    list: HeaderType []
}
function Header({ list }:Props) {
  return <ul className="header__list">
    { list.map((li, idx) => <li className="header__item" key={idx}><a href={li.link}>{li.displayName}</a></li>)}
  </ul>
}

export default Header
