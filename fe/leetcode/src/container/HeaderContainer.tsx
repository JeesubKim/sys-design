import Header from '../components/Header/Header'
// import './HeaderContainer.css'

const headers = [{
    "displayName":"Home",
    "link":"/"
},{
    "displayName":"Problems",
    "link":"/problems"
},{
    "displayName":"Leaderboards",
    "link":"/leaderboards"
}]

function HeaderContainer() {
  return <Header list={headers} />
}

export default HeaderContainer
