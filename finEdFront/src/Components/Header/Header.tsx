import { Link } from 'react-router-dom'
import styles from './Header.module.scss'
import logo from '../../assets/Screenshot 2024-04-12 145543.png'

function Header() {
    return (
        <div className={styles.HeaderWrapper}>
            <div className='logo'>
               <img src={logo} width={180} height={122} />
            </div>
            <div className={styles.LinkContainer}>
                <Link to="/home">Home</Link>
                <Link to="/about">About</Link>
                <Link to="/contact">Contact Us</Link>
                <Link to='/login'>
                    Profile
                    {/* @todo: Add image instead of text */}
                </Link>
            </div>
        </div>
    )
}

export default Header