import React from "react";
import BotResponse from "./BotResponse";
import "./IntroSection.css"; 
import InstagramIcon from '@mui/icons-material/Instagram';
import LinkedInIcon from '@mui/icons-material/LinkedIn';
import TwitterIcon from '@mui/icons-material/Twitter';

const IntroSection = () => {
  return (
    <div id="introsection" className="intro-section">
      <h1 className="heading" style={{ fontFamily: 'Anta, sans-serif', fontSize: '2.5rem', fontWeight: 'bold', color: '#333' }}>
        Introducing StockBot 
        <BotResponse response=" - Your Social Investment Assistant" />
      </h1>
      <h2 className="subtitle" style={{ fontFamily: 'Anta, sans-serif', fontSize: '1.3rem', color: '#666' }}>
        Welcome to StockBot, your personal AI-powered investment assistant
        brought to you by <span className="stockgro">Stockgro</span>. We believe in making investments social,
        and StockBot is here to revolutionize the way you interact with
        financial information.
      </h2>
      <h3 style={{ fontFamily: 'Anta, sans-serif', fontSize: '1.5rem', fontWeight: 'bold', color: '#333' }}>Features:</h3>
      <ul style={{ fontFamily: 'Anta, sans-serif', fontSize: '1.3rem', color: '#666' }}>
        <li>Instant answers to any investment-related question</li>
        <li>Powered by cutting-edge deep learning technology</li>
        <li>Continuously learning to provide better insights</li>
        <li>User-friendly interface designed for investors</li>
        <li>Available 24/7 to assist you with your investment queries</li>
      </ul>
      <p style={{ fontFamily: 'Anta, sans-serif', fontSize: '1.3rem', color: '#666' }}>
        Say goodbye to complicated financial jargon and endless searches for
        investment information. With StockBot, investing becomes social and
        accessible to everyone. Try it now and experience the future of
        investment assistance.
      </p>
      <h1 style={{ fontFamily: 'Anta, sans-serif', fontSize: '2rem', color: '#333' }}>
        Visit <a target="_blank" rel="noopener" href='https://www.stockgro.club/' alt='StockGro' style={{ textDecoration: 'none', color: '#007bff' }}>StockGro</a> for more information.
      </h1>
      <div className='header__socialhandles'>
        <h2 style={{ fontFamily: 'Anta, sans-serif', fontSize: '1.2rem', fontWeight: 'bold', color: '#333' }}>Connect with us on social media:</h2>
        <a target="_blank" rel="noopener" href='https://www.linkedin.com/company/stockgro/mycompany/' alt='LinkedIn'>
          <LinkedInIcon style={{ fontSize: '2.8rem', color:'black', marginRight: '10px' }} />
        </a>
        <a target="_blank" rel="noopener" href='https://twitter.com/stockgro' alt='Twitter'>
          <TwitterIcon style={{ fontSize: '2.8rem', color:'black', marginRight: '10px' }} />
        </a>
        <a target="_blank" rel="noopener" href='https://www.instagram.com/stock_gro?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==' alt='Instagram'>
          <InstagramIcon style={{ fontSize: '2.8rem', color:'black' }} />
        </a>
      </div>
    </div>

  );
};

export default IntroSection;
