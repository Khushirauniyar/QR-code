import React, { FC } from 'react';
import styles from './footer.module.css';

const Footer: FC = () => {
  return (
    <footer className={styles.footer}>
      <p>Made by 😎<a href ="https://github.com/ADi7YA26">Khushi Gupta</a>
      </p>
    </footer>
  );
};

export default Footer;
