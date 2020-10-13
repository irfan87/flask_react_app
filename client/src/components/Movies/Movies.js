import React, { useEffect, useState } from 'react'
import axios from 'axios';

export const Movies = () => {
    const [movies, setMovies] = useState([]);

    useEffect(() => {
        const fetchMovieData = async () => {
            const response = await axios.get('/movies');
            console.log(response.data.movies);

            setMovies(response.data.movies);
        }

        fetchMovieData();
    }, [])

    return (
        <div>
            <h1>Movies</h1>
            {movies.map(movie => {
                return(
                    <ul key={movie.name}>
                        <li>{movie.name}</li>
                    </ul>
                )
            })}
        </div>
    )
}
