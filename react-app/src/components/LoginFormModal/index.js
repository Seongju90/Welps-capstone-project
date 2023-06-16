import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    } else {
      closeModal()
    }
  };

  const demoUser = async (e) => {
    await dispatch(login('demo@aa.io', 'password'));
    closeModal()
  }


  return (
    <div className="login-container">
      <div className="login-text">Log In to Welps</div>
      <form className="login-form-container" onSubmit={handleSubmit}>
        <div className="demo-user-button"onClick={demoUser}>
          Demo user
        </div>
        <div className="login-divider">
          <span className="or">OR</span>
        </div>
        <input
          className="login-input-email"
          type="text"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
          placeholder="Email"
        />
        {errors.email && <div className="login-error-text">{errors.email}</div>}
        <input
          className="login-input-password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          placeholder="Password"
        />
        {errors.password && <div className="login-error-text">{errors.password}</div>}
        <button className="login-form-button"type="submit">Log In</button>
      </form>
    </div>
  );
}

export default LoginFormModal;
