import React from 'react';
import { useModal } from '../../context/Modal';
import updateIcon from '../../icons/update.svg';
import './EditRestaurantModalButton.css'

function EditRestaurantModalButton({
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
    <>
        <img
            className={buttonName} onClick={onClick}
            height={'16'}
            width={'16'}
            src={updateIcon}
            alt={'my-profile-update-icon'}
        />
    </>
  );
}

export default EditRestaurantModalButton;
