import { forwardRef } from "react";

const Input = forwardRef(function Input({ label, textarea, ...props }, ref) {
  return (
    <p>
      <label>{label}</label>
      {textarea ? (
        <textarea ref={ref} {...props}></textarea>
      ) : (
        <input ref={ref} {...props}></input>
      )}
    </p>
  );
});

export default Input;
