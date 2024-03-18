import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';

export default function Navigation(){


    return (
        <Navbar expand="lg" className="bg-sec p-3 border-bottom border-white ">
          <Container className='justify-content-center '>
            <Navbar.Brand href="#home" className='text-white fw-bold text-center'>Fintellitech</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
          </Container>
        </Navbar>
    );
}