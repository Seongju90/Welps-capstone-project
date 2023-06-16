import React from 'react';
import { useModal } from '../../context/Modal';
import star from '../../icons/star-svg2-com.svg'
import './OpenReviewModalButton.css'

function OpenReviewModalButton({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose, // optional: callback function that will be called once the modal is closed
  buttonName, // optional: className of button to style each separately
}) {
  const { setModalContent, setOnModalClose } = useModal();

  const onClick = () => {
    if (onModalClose) setOnModalClose(onModalClose);
    setModalContent(modalComponent);
    if (onButtonClick) onButtonClick();
  };

  return (
    <div className={buttonName} onClick={onClick}>
        <img
            className="star-svg-review"
            height={'24'}
            width={'24'}
            src={star}
            alt={'star-svg'}
        />
        <div className="single-index-button-text">{buttonText}</div>
    </div>
  );
}

export default OpenReviewModalButton;
