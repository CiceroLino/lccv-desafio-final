import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Contrato } from '../../shared/contratos.model';

@Injectable({
  providedIn: 'root'
})
export class ContratosService {

  constructor(public http: HttpClient) { }

  // private httpOptions = {header: new HttpHeaders({ 'Content-Type': 'application/json' })};
  // ERROR IN return this.http.get<Contrato[]>(this.contratosUrl, this.httpOptions);
  private contratosUrl = 'http://localhost:3000/contratos';

  getAll() : Observable<Contrato[]>{
    return this.http.get<Contrato[]>(this.contratosUrl);
  }

}
