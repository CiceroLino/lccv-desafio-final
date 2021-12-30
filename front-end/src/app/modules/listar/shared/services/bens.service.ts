import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Bens } from '../../../listar/shared/bens.model';


@Injectable({
  providedIn: 'root'
})
export class BensService {

  constructor(public http: HttpClient) { }

  // private httpOptions = {header: new HttpHeaders({ 'Content-Type': 'application/json' })};
  // ERROR IN return this.http.get<Contrato[]>(this.contratosUrl, this.httpOptions);
  private bensUrl = 'http://localhost:3000/bens';

  getAll() : Observable<Bens[]>{
    return this.http.get<Bens[]>(this.bensUrl);
  }
}
