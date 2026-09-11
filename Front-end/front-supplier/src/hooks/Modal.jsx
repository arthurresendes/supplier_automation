import styles from './modal.module.css'

const Modal = ({ isOpen, onClose, children }) => {
    if (!isOpen) return null;
    return (
        <div className={styles.overlay} onClick={onClose}>
            <div className={styles.content} onClick={(e) => e.stopPropagation()}>
                <div className={styles.header}>
                    <div className={styles.body}>
                        {children}
                    </div>
                    <button className={styles.closeButton} onClick={onClose}>✕</button>
                </div>
            </div>
        </div>
    );
}

export default Modal;