import { useRef, forwardRef, useImperativeHandle } from "react";
import { createPortal } from "react-dom";

const Modal = forwardRef(function Modal({ chilrdren }, ref) {
  const dialog = useRef();
  useImperativeHandle(ref, () => {
    return {
      open() {
        dialog.current.showModal();
      },
    };
  });

  return createPortal(
    <dialog ref={dialog}>
      {chilrdren}
      <form method="dialog">
        <button>Close</button>
      </form>
    </dialog>,
    document.getElementById('modal-root')
  );
});

export default Modal;
