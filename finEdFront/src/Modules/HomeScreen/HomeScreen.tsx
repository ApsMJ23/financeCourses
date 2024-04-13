import Header from '../../Components/Header/Header'
import styles from './HomeScreen.module.scss'
import {useNavigate} from 'react-router-dom';
import main_logo from '../../assets/Screenshot 2024-04-13 005554.png'
import bitcoin from '../../assets//Screenshot 2024-04-13 032910.png'

function HomeScreen() {
    const navigate = useNavigate()
    const gotToLoginPage=()=>{
        navigate('/LoginScreen');
      }
    return (
        <div>
            <Header />
            <div className={styles.LandingPageBanner}>

            </div>
            <div className={styles.main2}>
                <img src={main_logo} width={35} height={35} className={styles.image}/><p>FINancially FIT</p>
            </div>
            <div className={styles.main}>
                <p>A powerful platform for your financial</p><br/><p className={styles.text}>independence fitness</p>
                <p className={styles.text_1}>We make hardworking a habit for the<br/>people by motivating them for good.</p>
            </div>
            <button onClick={()=> gotToLoginPage()} className={styles.btn}>SIGN UP</button>
            <div className={styles.main_bottom}>
                <p>Why you should choose Fin Fit?</p>
            </div>
            <div className={styles.coin}>
                <p className={styles.poin}>Quality is at the heart of<br/> everything we do at FINFIT. <br/>We are committed to<br/>delivering the highest<br/>standards of education.</p>
                <img src={bitcoin} className={styles.iimg}/>
            </div>
            <div className={styles.green}>
                <p>Creating impact around the world</p>
                <div className={styles.green_text}>
                <p>75+<br/>Instructor</p>
                <p>1500+<br/>Inspired Student</p>
                <p>25+<br/>Courses</p>
            </div>
            <p className={styles.last}>Skills are the key<br/>to unlocking<br/>potential</p>
            </div>
        </div>
        
    )
}

export default HomeScreen;